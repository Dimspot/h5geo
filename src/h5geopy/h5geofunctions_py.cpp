#include "../../include/h5geopy/h5geofunctions_py.h"

#include <h5geo/h5mapcontainer.h>
#include <h5geo/h5map.h>
#include <h5geo/h5wellcontainer.h>
#include <h5geo/h5well.h>
#include <h5geo/h5seiscontainer.h>
#include <h5geo/h5seis.h>
#include <h5geo/h5core.h>

namespace h5geopy {

namespace ext {

std::tuple<std::vector<std::string>, std::vector<std::string>>
getTraceHeaderNames()
{
  std::vector<std::string> fullHeaderNames, shortHeaderNames;
  h5geo::getTraceHeaderNames(fullHeaderNames, shortHeaderNames);
  return std::make_tuple(fullHeaderNames, shortHeaderNames);
}

std::tuple<std::vector<std::string>, std::vector<std::string>>
getBinHeaderNames()
{
  std::vector<std::string> fullHeaderNames, shortHeaderNames;
  h5geo::getBinHeaderNames(fullHeaderNames, shortHeaderNames);
  return std::make_tuple(fullHeaderNames, shortHeaderNames);
}

std::tuple<std::vector<int>, std::vector<int>>
getTraceHeaderBytes()
{
  std::vector<int> bytesStart, nBytes;
  h5geo::getTraceHeaderBytes(bytesStart, nBytes);
  return std::make_tuple(bytesStart, nBytes);
}

std::tuple<std::vector<int>, std::vector<int>>
getBinHeaderBytes()
{
  std::vector<int> bytesStart, nBytes;
  h5geo::getBinHeaderBytes(bytesStart, nBytes);
  return std::make_tuple(bytesStart, nBytes);
}

} // ext


void defineGeoFunctions(py::module_& m){
  m.def("openBaseContainer", &openBaseContainer);
  m.def("openBaseContainerByName", &openBaseContainerByName);
  m.def("openBaseObject", &openBaseObject);
  m.def("openSeisContainer", &openSeisContainer);
  m.def("openSeisContainerByName", &openSeisContainerByName);
  m.def("openMapContainerByName", &openMapContainerByName);
  m.def("openWellContainer", &openWellContainer);
  m.def("openWellContainerByName", &openWellContainerByName);

  m.def("createMapContainer", &createMapContainer);
  m.def("createMapContainerByName", &createMapContainerByName);
  m.def("createWellContainer", &createWellContainer);
  m.def("createWellContainerByName", &createWellContainerByName);
  m.def("createSeisContainer", &createSeisContainer);
  m.def("createSeisContainerByName", &createSeisContainerByName);

  m.def("isGeoContainer", &isGeoContainer);
  m.def("isGeoContainerByType", &isGeoContainerByType);
  m.def("isGeoObject", &isGeoObject);
  m.def("isGeoObjectByType", &isGeoObjectByType);
  m.def("isMap", &isMap);
  m.def("isWell", &isWell);
  m.def("isLogCurve", &isLogCurve);
  m.def("isDevCurve", &isDevCurve);
  m.def("isSeis", &isSeis);

  m.def("getTraceHeaderNames", &ext::getTraceHeaderNames);
  m.def("getBinHeaderNames", &ext::getTraceHeaderNames);
  m.def("getTraceHeaderBytes", &ext::getTraceHeaderNames);
  m.def("getBinHeaderBytes", &ext::getTraceHeaderNames);
  m.def("getTraceHeaderCount", &getTraceHeaderNames);
  m.def("getBinHeaderCount", &getTraceHeaderNames);
}


} // h5geopy
