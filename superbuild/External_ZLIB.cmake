message("external project: ZLIB")

# SET DIRS
set(EP_SOURCE_DIR "${CMAKE_BINARY_DIR}/zlib")
set(EP_BINARY_DIR "${CMAKE_BINARY_DIR}/zlib-build")
set(EP_INSTALL_DIR "${CMAKE_INSTALL_PREFIX}/zlib-install")
list(APPEND CMAKE_PREFIX_PATH "${EP_SOURCE_DIR}")

#-----------------------------------------------------------------------------
set(ZLIB_ROOT PATH ${EP_INSTALL_DIR})
find_package(ZLIB)

set(DEPENDENCIES "")

if(NOT DEFINED ZLIB_FOUND OR NOT ZLIB_FOUND)
  ExternalProject_Add(ZLIB
    GIT_REPOSITORY "https://github.com/madler/zlib.git"
    GIT_TAG "v1.2.11"
    SOURCE_DIR ${EP_SOURCE_DIR}
    BINARY_DIR ${EP_BINARY_DIR}
    INSTALL_DIR ${EP_INSTALL_DIR}
    CMAKE_CACHE_ARGS
      # Compiler settings
      -DCMAKE_CXX_COMPILER:FILEPATH=${CMAKE_CXX_COMPILER}
      -DCMAKE_C_COMPILER:FILEPATH=${CMAKE_C_COMPILER}
      -DCMAKE_CXX_STANDARD:STRING=${CMAKE_CXX_STANDARD}
      -DCMAKE_CXX_STANDARD_REQUIRED:BOOL=${CMAKE_CXX_STANDARD_REQUIRED}
      -DCMAKE_CXX_EXTENSIONS:BOOL=${CMAKE_CXX_EXTENSIONS}
      -DCMAKE_INSTALL_PREFIX:PATH=<INSTALL_DIR>
      -DINSTALL_BIN_DIR:PATH=<INSTALL_DIR>/bin
      -DINSTALL_INC_DIR:PATH=<INSTALL_DIR>/include
      -DINSTALL_LIB_DIR:PATH=<INSTALL_DIR>/lib
      -DINSTALL_MAN_DIR:PATH=<INSTALL_DIR>/share/man
      -DINSTALL_PKGCONFIG_DIR:PATH=<INSTALL_DIR>/share/pkgconfig
    DEPENDS ${DEPENDENCIES}
    )
else()
  # Add empty project that exports target ZLIB
  ExternalProject_Add(ZLIB
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
