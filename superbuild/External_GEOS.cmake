message("external project: GEOS")

# SET DIRS
set(EP_SOURCE_DIR "${CMAKE_BINARY_DIR}/GEOS")
set(EP_BINARY_DIR "${CMAKE_BINARY_DIR}/GEOS-build")
set(EP_INSTALL_DIR "${CMAKE_INSTALL_PREFIX}/GEOS-install")
list(APPEND CMAKE_PREFIX_PATH ${EP_INSTALL_DIR})

#-----------------------------------------------------------------------------
set(GEOS_ROOT ${EP_INSTALL_DIR})
set(GEOS_DIR "${GEOS_ROOT}/lib/cmake/GEOS")
find_package(GEOS)

if(WIN32)
  list(APPEND GDAL_RUNTIME_DIR "${GEOS_ROOT}/bin")
  set(GEOS_LIBRARIES "${GEOS_ROOT}/lib/geos_c.lib;${GEOS_ROOT}/lib/geos.lib")
else()
  list(APPEND GDAL_RUNTIME_DIR "${GEOS_ROOT}/lib")
  set(GEOS_LIBRARIES "${GEOS_ROOT}/lib/libgeos_c.so;${GEOS_ROOT}/lib/libgeos.so")
endif()

set(DEPENDENCIES "")

if(NOT DEFINED GEOS_FOUND OR NOT GEOS_FOUND)
  ExternalProject_Add(GEOS
    GIT_REPOSITORY "https://github.com/libgeos/geos.git"
    GIT_TAG "3.10.2"
    SOURCE_DIR ${EP_SOURCE_DIR}
    BINARY_DIR ${EP_BINARY_DIR}
    INSTALL_DIR ${EP_INSTALL_DIR}
    CMAKE_CACHE_ARGS
      # CMake settings
      -DCMAKE_CXX_COMPILER:FILEPATH=${CMAKE_CXX_COMPILER}
      -DCMAKE_C_COMPILER:FILEPATH=${CMAKE_C_COMPILER}
      -DCMAKE_CXX_STANDARD:STRING=${CMAKE_CXX_STANDARD}
      -DCMAKE_CXX_STANDARD_REQUIRED:BOOL=${CMAKE_CXX_STANDARD_REQUIRED}
      -DCMAKE_CXX_EXTENSIONS:BOOL=${CMAKE_CXX_EXTENSIONS}
      -DCMAKE_INSTALL_PREFIX:PATH=<INSTALL_DIR>
      # Lib settings
      -DBUILD_TESTING:BOOL=OFF
    DEPENDS ${DEPENDENCIES}
    )
else()
  # Add empty project that exports target GEOS
  ExternalProject_Add(GEOS
    SOURCE_DIR ${EP_SOURCE_DIR}
    BINARY_DIR ${EP_BINARY_DIR}
    INSTALL_DIR ${EP_INSTALL_DIR}
    DOWNLOAD_COMMAND ""
    CONFIGURE_COMMAND ""
    BUILD_COMMAND ""
    INSTALL_COMMAND ""
    DEPENDS ${DEPENDENCIES}
    )
endif()
