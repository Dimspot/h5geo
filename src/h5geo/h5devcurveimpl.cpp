#include "../../include/h5geo/misc/h5devcurveimpl.h"
#include "../../include/h5geo/h5wellcontainer.h"
#include "../../include/h5geo/h5core.h"
#include "../../include/h5geo/misc/h5wellimpl.h"

H5DevCurveImpl::H5DevCurveImpl(const h5gt::Group &group) :
  H5BaseObjectImpl(group){}

bool H5DevCurveImpl::writeCurve(
    const h5geo::DevDataType& name,
    const Eigen::Ref<const Eigen::VectorXd>& v)
{
  return writeCurve(
        std::string{magic_enum::enum_name(name)}, v);
}

bool H5DevCurveImpl::writeCurve(
    const std::string& name,
    const Eigen::Ref<const Eigen::VectorXd>& v)
{
  auto opt = getDevCurveD();
  if (!opt.has_value())
    return false;

  return h5geo::writeData2IndexedDataset(
        opt.value(),
        name,
        v,
        true);
}

bool H5DevCurveImpl::setActive(){
  auto optWellG = getParentG(h5geo::ObjectType::WELL);
  if (!optWellG.has_value())
    return false;

  H5WellImpl well(optWellG.value());

  return well.setActiveDevCurve(*this);
}

bool H5DevCurveImpl::isActive(){
  auto optWellG = getParentG(h5geo::ObjectType::WELL);
  if (!optWellG.has_value())
    return false;

  H5WellImpl well(optWellG.value());

  auto optActiveDevG = well.getActiveDevG();
  if (!optActiveDevG.has_value())
    return false;

  H5DevCurveImpl activeDev(optActiveDevG.value());
  return *this == activeDev;
}

size_t H5DevCurveImpl::getNCurves(){
  auto opt = getDevCurveD();
  if (!opt.has_value())
    return 0;

  return opt->getDimensions()[0];
}

size_t H5DevCurveImpl::getNSamp(){
  auto opt = getDevCurveD();
  if (!opt.has_value())
    return 0;

  return opt->getDimensions()[1];
}

Eigen::VectorXd H5DevCurveImpl::getCurve(
    const h5geo::DevDataType& name)
{
  return getCurve(std::string{magic_enum::enum_name(name)});
}

Eigen::VectorXd H5DevCurveImpl::getCurve(
    const std::string& name)
{
  auto opt = getDevCurveD();
  if (!opt.has_value())
    return Eigen::VectorXd();

  return h5geo::getDataFromIndexedDataset<double>(
        opt.value(), name);
}

std::string H5DevCurveImpl::getRelativeCurveName(){
  auto optWellG = getParentG(h5geo::ObjectType::WELL);
  if (!optWellG.has_value())
    return std::string();

  H5WellImpl well(optWellG.value());
  auto optDevG = well.getDevG();
  if (!optDevG.has_value())
    return std::string();

  return h5geo::getRelativePath(
        optDevG->getPath(), objG.getPath(),
        h5geo::CaseSensitivity::CASE_INSENSITIVE);
}

H5WellContainer* H5DevCurveImpl::getWellContainer(){
  h5gt::File file = getH5File();
  return h5geo::createWellContainer(
        file, h5geo::CreationType::OPEN_OR_CREATE);
}

H5Well* H5DevCurveImpl::getWell()
{
  auto optWellG = getParentG(h5geo::ObjectType::WELL);
  if (!optWellG.has_value())
    return nullptr;

  return new H5WellImpl(optWellG.value());
}

std::optional<h5gt::DataSet>
H5DevCurveImpl::getDevCurveD()
{
  std::string name = std::string{magic_enum::enum_name(
        h5geo::detail::DevDatasets::dev_data)};

  return getDatasetOpt(objG, name);
}