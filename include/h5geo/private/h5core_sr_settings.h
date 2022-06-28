#ifndef H5CORE_SR_SETTINGS_H
#define H5CORE_SR_SETTINGS_H

#include "h5geo_export.h"
#include "h5enum.h"

#include <string>

#include <Eigen/Dense>

class OGRSpatialReference;

namespace h5geo
{


namespace sr {


H5GEO_EXPORT void setSpatialReference(OGRSpatialReference sr);
H5GEO_EXPORT void setSpatialReferenceFromUserInput(
    const std::string& name);
H5GEO_EXPORT void setSpatialReferenceFromUserInput(
    const std::string& authName, const std::string& code);
H5GEO_EXPORT OGRSpatialReference getSpatialReference();

H5GEO_EXPORT void setLengthUnits(const std::string& units);
H5GEO_EXPORT void setAngularUnits(const std::string& units);
H5GEO_EXPORT void setTemporalUnits(const std::string& units);

H5GEO_EXPORT std::string getLengthUnits();
H5GEO_EXPORT std::string getAngularUnits();
H5GEO_EXPORT std::string getTemporalUnits();

H5GEO_EXPORT void setDomain(const std::string& domain);
H5GEO_EXPORT void setDomain(const h5geo::Domain& domain);

H5GEO_EXPORT std::string getDomain();
H5GEO_EXPORT h5geo::Domain getDomainEnum();

H5GEO_EXPORT bool convertUnits(
    Eigen::Ref<Eigen::MatrixXd> m,
    const std::string& unitsFrom,
    const std::string& unitsTo);
H5GEO_EXPORT bool convertUnits(
    Eigen::Ref<Eigen::MatrixXf> m,
    const std::string& unitsFrom,
    const std::string& unitsTo);

// Transform coord FROM
/// Transform from given CRS to the project CRS
H5GEO_EXPORT bool transformCoordFrom(
    Eigen::Ref<Eigen::MatrixXd> x,
    Eigen::Ref<Eigen::MatrixXd> y,
    const std::string& unitsFrom,
    const std::string& srAuthAndCodeFrom);
/// Transform from given CRS to the project CRS
H5GEO_EXPORT bool transformCoordFrom(
    Eigen::Ref<Eigen::MatrixXd> x,
    Eigen::Ref<Eigen::MatrixXd> y,
    const std::string& unitsFrom,
    const std::string& authNameFrom,
    const std::string& codeFrom);
/// Transform from given CRS to the project CRS
H5GEO_EXPORT bool transformCoordFrom(
    Eigen::Ref<Eigen::MatrixXf> x,
    Eigen::Ref<Eigen::MatrixXf> y,
    const std::string& unitsFrom,
    const std::string& srAuthAndCodeFrom);
/// Transform from given CRS to the project CRS
H5GEO_EXPORT bool transformCoordFrom(
    Eigen::Ref<Eigen::MatrixXf> x,
    Eigen::Ref<Eigen::MatrixXf> y,
    const std::string& unitsFrom,
    const std::string& authNameFrom,
    const std::string& codeFrom);


// Transform coord TO
/// Transform from project CRS to the given CRS
H5GEO_EXPORT bool transformCoordTo(
    Eigen::Ref<Eigen::MatrixXd> x,
    Eigen::Ref<Eigen::MatrixXd> y,
    const std::string& unitsTo,
    const std::string& srAuthAndCodeTo);
/// Transform from project CRS to the given CRS
H5GEO_EXPORT bool transformCoordTo(
    Eigen::Ref<Eigen::MatrixXd> x,
    Eigen::Ref<Eigen::MatrixXd> y,
    const std::string& unitsTo,
    const std::string& authNameTo,
    const std::string& codeTo);
/// Transform from project CRS to the given CRS
H5GEO_EXPORT bool transformCoordTo(
    Eigen::Ref<Eigen::MatrixXf> x,
    Eigen::Ref<Eigen::MatrixXf> y,
    const std::string& unitsTo,
    const std::string& srAuthAndCodeTo);
/// Transform from project CRS to the given CRS
H5GEO_EXPORT bool transformCoordTo(
    Eigen::Ref<Eigen::MatrixXf> x,
    Eigen::Ref<Eigen::MatrixXf> y,
    const std::string& unitsTo,
    const std::string& authNameTo,
    const std::string& codeTo);


} // sr


} // h5geo


#endif // H5CORE_SR_SETTINGS_H