cmake_minimum_required(VERSION 3.21)

include(cmake/prelude.cmake)

project(
    framewase-website-manager
    VERSION 0.0.1
    DESCRIPTION "A feature-rich user-friendly website manager for the official Framewase ecosystem"
    HOMEPAGE_URL "https://example.com/"
    LANGUAGES C
)

set(CMAKE_C_STANDARD_REQUIRED ON)

include(cmake/variables.cmake)

# ---- Declare executable ----

find_package(PkgConfig REQUIRED)

pkg_check_modules(GTK3 REQUIRED IMPORTED_TARGET gtk+-3.0)

add_executable(framewase-website-manager_exe source/main.c source/ui/slider_size_entry.c
  source/input/setup.h)
add_executable(framewase-website-manager::exe ALIAS framewase-website-manager_exe)

set_property(TARGET framewase-website-manager_exe PROPERTY OUTPUT_NAME framewase-website-manager)

target_compile_features(framewase-website-manager_exe PRIVATE c_std_99)

target_include_directories(framewase-website-manager_exe PRIVATE ${CMAKE_CURRENT_SOURCE_DIR}/source)

target_link_libraries(framewase-website-manager_exe PRIVATE PkgConfig::GTK3 m)

# ---- Install rules ----

if(NOT CMAKE_SKIP_INSTALL_RULES)
  include(cmake/install-rules.cmake)
endif()

# ---- Developer mode ----

if(NOT framewase-website-manager_DEVELOPER_MODE)
  return()
elseif(NOT PROJECT_IS_TOP_LEVEL)
  message(
      AUTHOR_WARNING
      "Developer mode is intended for developers of framewase-website-manager"
  )
endif()

include(cmake/dev-mode.cmake)
