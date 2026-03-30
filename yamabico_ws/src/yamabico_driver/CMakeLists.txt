cmake_minimum_required(VERSION 3.5)
project(yamabico_driver)

find_package(ament_cmake_auto REQUIRED)
ament_auto_find_build_dependencies()

ament_auto_add_executable(yamabico_driver
  src/yamabico_driver_node.cpp)

target_link_libraries(yamabico_driver ypspur)

target_include_directories(yamabico_driver
  PUBLIC ${ypspur_INCLUDE_DIRS})

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  ament_lint_auto_find_test_dependencies()
endif()

ament_auto_package(
  INSTALL_TO_SHARE
  config
  launch
  scripts
)
