#include "../../include/h5geopy/h5logcurve_py.h"

#include <h5geo/misc/h5wellcontainerimpl.h>
#include <h5geo/misc/h5wellimpl.h>

namespace h5geopy {

void H5LogCurve_py(
    py::class_<
    H5LogCurveImpl,
    std::unique_ptr<H5LogCurveImpl, ObjectDeleter>,
    H5BaseObjectImpl,
    H5LogCurve> &py_obj){
  py_obj
      .def("writeCurve", py::overload_cast<const LogDataType&,
           const Eigen::Ref<const Eigen::VectorXd>&, const std::string&>(
             &H5LogCurveImpl::writeCurve),
           py::arg("name"), py::arg("data"), py::arg_v("units", "", "str()"))
      .def("writeCurve", py::overload_cast<const std::string&,
           const Eigen::Ref<const Eigen::VectorXd>&, const std::string&>(
             &H5LogCurveImpl::writeCurve),
           py::arg("name"), py::arg("data"), py::arg_v("units", "", "str()"))

      .def("getCurve", py::overload_cast<const LogDataType&, const std::string&>(&H5LogCurveImpl::getCurve),
           py::arg("name"), py::arg_v("units", "", "str()"))
      .def("getCurve", py::overload_cast<const std::string&, const std::string&>(&H5LogCurveImpl::getCurve),
           py::arg("name"), py::arg_v("units", "", "str()"))

      .def("setSpatialUnits", &H5LogCurve::setSpatialUnits)
      .def("setDataUnits", &H5LogCurve::setDataUnits)

      .def("getSpatialUnits", &H5LogCurve::getSpatialUnits)
      .def("getDataUnits", &H5LogCurve::getDataUnits)

      .def("getRelativeCurveName", &H5LogCurveImpl::getRelativeCurveName)

      .def("getWellContainer", &H5LogCurveImpl::getWellContainer)
      .def("getWell", &H5LogCurveImpl::getWell)

      .def("getLogCurveD", &H5LogCurveImpl::getLogCurveD);
}


} // h5geopy
