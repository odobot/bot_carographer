cmake_minimum_required(VERSION 3.8)
project(bot_carographer)

set(bot_carographer_MAJOR_VERSION 0)
set(bot_carographer_MINOR_VERSION 0)
set(bot_carographer_PATCH_VERSION 0)
set(bot_carographer_VERSION
  ${bot_carographer_MAJOR_VERSION}.${bot_carographer_MINOR_VERSION}.${bot_carographer_PATCH_VERSION})

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# uncomment the following section in order to fill in
# further dependencies manually.
# find_package(<dependency> REQUIRED)
find_package(cartographer REQUIRED)
find_package(ament_cmake REQUIRED)
find_package(urdf REQUIRED)

install(DIRECTORY urdf launch configuration
  DESTINATION share/${PROJECT_NAME}
)

ament_package()