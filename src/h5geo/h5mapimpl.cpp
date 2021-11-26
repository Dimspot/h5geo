#include "../../include/h5geo/misc/h5mapimpl.h"
#include "../../include/h5geo/h5mapcontainer.h"
#include "../../include/h5geo/h5core.h"
#include "../../include/h5geo/misc/h5core_enum_string.h"

#include <units/units.hpp>

#ifdef H5GEO_USE_GDAL
#include <gdal/gdal.h>
#include <gdal/gdal_priv.h>
#endif

H5MapImpl::H5MapImpl(const h5gt::Group &group) :
  H5BaseObjectImpl(group){}

bool H5MapImpl::writeData(
    Eigen::Ref<Eigen::MatrixXd> M,
    const std::string& dataUnits)
{
  auto opt = getMapD();
  if (!opt.has_value())
    return false;

  return h5geo::overwriteResizableDataset(
        objG,
        opt->getPath(),
        M,
        dataUnits, getDataUnits());
}

Eigen::MatrixXd H5MapImpl::getData(const std::string& dataUnits){
  auto opt = getMapD();
  if (!opt.has_value())
    return Eigen::MatrixXd();

  return h5geo::readDoubleEigenMtxDataset(
        objG,
        opt->getPath(),
        getDataUnits(), dataUnits);
}

bool H5MapImpl::setDomain(const h5geo::Domain& val){
  unsigned v = static_cast<unsigned>(val);
  return h5geo::overwriteAttribute(
        objG,
        std::string{h5geo::detail::Domain},
        v);
}

bool H5MapImpl::setOrigin(
    Eigen::Ref<Eigen::Vector2d> v,
    const std::string& spatialUnits,
    bool doCoordTransform)
{
#ifdef H5GEO_USE_GDAL
  if (doCoordTransform){
    OGRCoordinateTransformation* coordTrans =
        createCoordinateTransformationToWriteData(spatialUnits);
    if (!coordTrans)
      return false;

    coordTrans->Transform(1, &v(0), &v(1));
    return h5geo::overwriteAttribute(
          objG,
          std::string{h5geo::detail::origin},
          v);
  }
#endif

  return h5geo::overwriteAttribute(
        objG,
        std::string{h5geo::detail::origin},
        v, spatialUnits, getSpatialUnits());
}

bool H5MapImpl::setPoint1(
    Eigen::Ref<Eigen::Vector2d> v,
    const std::string& spatialUnits,
    bool doCoordTransform)
{
#ifdef H5GEO_USE_GDAL
  if (doCoordTransform){
    OGRCoordinateTransformation* coordTrans =
        createCoordinateTransformationToWriteData(spatialUnits);
    if (!coordTrans)
      return false;

    coordTrans->Transform(1, &v(0), &v(1));
    return h5geo::overwriteAttribute(
          objG,
          std::string{h5geo::detail::point1},
          v);
  }
#endif

  return h5geo::overwriteAttribute(
        objG,
        std::string{h5geo::detail::point1},
        v, spatialUnits, getSpatialUnits());
}

bool H5MapImpl::setPoint2(
    Eigen::Ref<Eigen::Vector2d> v,
    const std::string& spatialUnits,
    bool doCoordTransform){
#ifdef H5GEO_USE_GDAL
  if (doCoordTransform){
    OGRCoordinateTransformation* coordTrans =
        createCoordinateTransformationToWriteData(spatialUnits);
    if (!coordTrans)
      return false;

    coordTrans->Transform(1, &v(0), &v(1));
    return h5geo::overwriteAttribute(
          objG,
          std::string{h5geo::detail::point2},
          v);
  }
#endif

  return h5geo::overwriteAttribute(
        objG,
        std::string{h5geo::detail::point2},
        v, spatialUnits, getSpatialUnits());
}

bool H5MapImpl::addAttribute(H5Map* map, std::string name){
  if (this->getH5File() != map->getH5File())
    return false;

  if (name.empty())
    name = map->getName();

  if (objG.hasObject(name, h5gt::ObjectType::Group))
    return false;

  objG.createLink(map->getObjG(), name, h5gt::LinkType::Soft);
  return true;
}

bool H5MapImpl::addExternalAttribute(H5Map* map, std::string name){
  if (this->getH5File() == map->getH5File())
    return false;

  if (name.empty())
    name = map->getName();

  if (objG.hasObject(name, h5gt::ObjectType::Group))
    return false;

  objG.createLink(map->getObjG(), name, h5gt::LinkType::External);
  return true;
}

bool H5MapImpl::removeAttribute(const std::string& name){
  if (name.empty())
    return false;

  if (!objG.hasObject(name, h5gt::ObjectType::Group))
    return false;

  objG.unlink(name);
  return true;
}

H5Map* H5MapImpl::getAttribute(const std::string& name){
  if (!objG.hasObject(name, h5gt::ObjectType::Group))
    return nullptr;

  h5gt::Group group = objG.getGroup(name);
  if (!isGeoObjectByType(group, h5geo::ObjectType::MAP))
    return nullptr;

  return new H5MapImpl(group);
}

h5geo::Domain H5MapImpl::getDomain(){
  return static_cast<h5geo::Domain>(
        h5geo::readEnumAttribute(
          objG,
          std::string{h5geo::detail::Domain}));
}

Eigen::VectorXd H5MapImpl::getOrigin(
    const std::string& spatialUnits,
    bool doCoordTransform)
{
#ifdef H5GEO_USE_GDAL
  if (doCoordTransform){
    OGRCoordinateTransformation* coordTrans =
        createCoordinateTransformationToReadData(spatialUnits);
    if (!coordTrans)
      return Eigen::VectorXd();

    Eigen::VectorXd v = h5geo::readDoubleEigenVecAttribute(
          objG,
          std::string{h5geo::detail::origin});

    if (v.size() != 2)
      return Eigen::VectorXd();

    coordTrans->Transform(1, &v(0), &v(1));
    return v;
  }
#endif

  return h5geo::readDoubleEigenVecAttribute(
        objG,
        std::string{h5geo::detail::origin},
        getSpatialUnits(), spatialUnits);
}

Eigen::VectorXd H5MapImpl::getPoint1(
    const std::string& spatialUnits,
    bool doCoordTransform)
{
#ifdef H5GEO_USE_GDAL
  if (doCoordTransform){
    OGRCoordinateTransformation* coordTrans =
        createCoordinateTransformationToReadData(spatialUnits);
    if (!coordTrans)
      return Eigen::VectorXd();

    Eigen::VectorXd v = h5geo::readDoubleEigenVecAttribute(
          objG,
          std::string{h5geo::detail::point1});

    if (v.size() != 2)
      return Eigen::VectorXd();

    coordTrans->Transform(1, &v(0), &v(1));
    return v;
  }
#endif

  return h5geo::readDoubleEigenVecAttribute(
        objG,
        std::string{h5geo::detail::point1},
        getSpatialUnits(), spatialUnits);
}

Eigen::VectorXd H5MapImpl::getPoint2(
    const std::string& spatialUnits,
    bool doCoordTransform)
{
#ifdef H5GEO_USE_GDAL
  if (doCoordTransform){
    OGRCoordinateTransformation* coordTrans =
        createCoordinateTransformationToReadData(spatialUnits);
    if (!coordTrans)
      return Eigen::VectorXd();

    Eigen::VectorXd v = h5geo::readDoubleEigenVecAttribute(
          objG,
          std::string{h5geo::detail::point2});

    if (v.size() != 2)
      return Eigen::VectorXd();

    coordTrans->Transform(1, &v(0), &v(1));
    return v;
  }
#endif

  return h5geo::readDoubleEigenVecAttribute(
        objG,
        std::string{h5geo::detail::point2},
        getSpatialUnits(), spatialUnits);
}


H5MapContainer* H5MapImpl::getMapContainer() const{
  h5gt::File file = getH5File();
  return h5geo::createMapContainer(
        file, h5geo::CreationType::OPEN_OR_CREATE);
}

std::optional<h5gt::DataSet>
H5MapImpl::getMapD() const
{
  std::string name = std::string{magic_enum::enum_name(
        h5geo::detail::MapDatasets::map_data)};

  return getDatasetOpt(objG, name);
}

H5Map* h5geo::openMap(h5gt::Group group){
  if (isGeoObjectByType(group, h5geo::ObjectType::MAP))
      return new H5MapImpl(group);

  return nullptr;
}