# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "joystick: 1 messages, 0 services")

set(MSG_I_FLAGS "-Ijoystick:/home/n9646/catkin_ws_car/src/joystick/msg;-Istd_msgs:/opt/ros/melodic/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(joystick_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/n9646/catkin_ws_car/src/joystick/msg/JoyStick.msg" NAME_WE)
add_custom_target(_joystick_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "joystick" "/home/n9646/catkin_ws_car/src/joystick/msg/JoyStick.msg" ""
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(joystick
  "/home/n9646/catkin_ws_car/src/joystick/msg/JoyStick.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/joystick
)

### Generating Services

### Generating Module File
_generate_module_cpp(joystick
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/joystick
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(joystick_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(joystick_generate_messages joystick_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/n9646/catkin_ws_car/src/joystick/msg/JoyStick.msg" NAME_WE)
add_dependencies(joystick_generate_messages_cpp _joystick_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(joystick_gencpp)
add_dependencies(joystick_gencpp joystick_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS joystick_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(joystick
  "/home/n9646/catkin_ws_car/src/joystick/msg/JoyStick.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/joystick
)

### Generating Services

### Generating Module File
_generate_module_eus(joystick
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/joystick
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(joystick_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(joystick_generate_messages joystick_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/n9646/catkin_ws_car/src/joystick/msg/JoyStick.msg" NAME_WE)
add_dependencies(joystick_generate_messages_eus _joystick_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(joystick_geneus)
add_dependencies(joystick_geneus joystick_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS joystick_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(joystick
  "/home/n9646/catkin_ws_car/src/joystick/msg/JoyStick.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/joystick
)

### Generating Services

### Generating Module File
_generate_module_lisp(joystick
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/joystick
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(joystick_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(joystick_generate_messages joystick_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/n9646/catkin_ws_car/src/joystick/msg/JoyStick.msg" NAME_WE)
add_dependencies(joystick_generate_messages_lisp _joystick_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(joystick_genlisp)
add_dependencies(joystick_genlisp joystick_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS joystick_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(joystick
  "/home/n9646/catkin_ws_car/src/joystick/msg/JoyStick.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/joystick
)

### Generating Services

### Generating Module File
_generate_module_nodejs(joystick
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/joystick
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(joystick_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(joystick_generate_messages joystick_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/n9646/catkin_ws_car/src/joystick/msg/JoyStick.msg" NAME_WE)
add_dependencies(joystick_generate_messages_nodejs _joystick_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(joystick_gennodejs)
add_dependencies(joystick_gennodejs joystick_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS joystick_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(joystick
  "/home/n9646/catkin_ws_car/src/joystick/msg/JoyStick.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/joystick
)

### Generating Services

### Generating Module File
_generate_module_py(joystick
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/joystick
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(joystick_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(joystick_generate_messages joystick_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/n9646/catkin_ws_car/src/joystick/msg/JoyStick.msg" NAME_WE)
add_dependencies(joystick_generate_messages_py _joystick_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(joystick_genpy)
add_dependencies(joystick_genpy joystick_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS joystick_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/joystick)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/joystick
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(joystick_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/joystick)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/joystick
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(joystick_generate_messages_eus std_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/joystick)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/joystick
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(joystick_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/joystick)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/joystick
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(joystick_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/joystick)
  install(CODE "execute_process(COMMAND \"/usr/bin/python2\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/joystick\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/joystick
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(joystick_generate_messages_py std_msgs_generate_messages_py)
endif()
