# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.16

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/ljb/crazyswarm/ros_ws/src/externalDependencies/libmotioncapture

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/ljb/crazyswarm/ros_ws/src/externalDependencies/libmotioncapture/build

# Include any dependencies generated for this target.
include externalDependencies/vicon-datastream-sdk/CMakeFiles/ViconDataStreamSDK_CPPTest.dir/depend.make

# Include the progress variables for this target.
include externalDependencies/vicon-datastream-sdk/CMakeFiles/ViconDataStreamSDK_CPPTest.dir/progress.make

# Include the compile flags for this target's objects.
include externalDependencies/vicon-datastream-sdk/CMakeFiles/ViconDataStreamSDK_CPPTest.dir/flags.make

externalDependencies/vicon-datastream-sdk/CMakeFiles/ViconDataStreamSDK_CPPTest.dir/Vicon/CrossMarket/DataStream/ViconDataStreamSDK_CPPTest/ViconDataStreamSDK_CPPTest.cpp.o: externalDependencies/vicon-datastream-sdk/CMakeFiles/ViconDataStreamSDK_CPPTest.dir/flags.make
externalDependencies/vicon-datastream-sdk/CMakeFiles/ViconDataStreamSDK_CPPTest.dir/Vicon/CrossMarket/DataStream/ViconDataStreamSDK_CPPTest/ViconDataStreamSDK_CPPTest.cpp.o: ../externalDependencies/vicon-datastream-sdk/Vicon/CrossMarket/DataStream/ViconDataStreamSDK_CPPTest/ViconDataStreamSDK_CPPTest.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/ljb/crazyswarm/ros_ws/src/externalDependencies/libmotioncapture/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object externalDependencies/vicon-datastream-sdk/CMakeFiles/ViconDataStreamSDK_CPPTest.dir/Vicon/CrossMarket/DataStream/ViconDataStreamSDK_CPPTest/ViconDataStreamSDK_CPPTest.cpp.o"
	cd /home/ljb/crazyswarm/ros_ws/src/externalDependencies/libmotioncapture/build/externalDependencies/vicon-datastream-sdk && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/ViconDataStreamSDK_CPPTest.dir/Vicon/CrossMarket/DataStream/ViconDataStreamSDK_CPPTest/ViconDataStreamSDK_CPPTest.cpp.o -c /home/ljb/crazyswarm/ros_ws/src/externalDependencies/libmotioncapture/externalDependencies/vicon-datastream-sdk/Vicon/CrossMarket/DataStream/ViconDataStreamSDK_CPPTest/ViconDataStreamSDK_CPPTest.cpp

externalDependencies/vicon-datastream-sdk/CMakeFiles/ViconDataStreamSDK_CPPTest.dir/Vicon/CrossMarket/DataStream/ViconDataStreamSDK_CPPTest/ViconDataStreamSDK_CPPTest.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/ViconDataStreamSDK_CPPTest.dir/Vicon/CrossMarket/DataStream/ViconDataStreamSDK_CPPTest/ViconDataStreamSDK_CPPTest.cpp.i"
	cd /home/ljb/crazyswarm/ros_ws/src/externalDependencies/libmotioncapture/build/externalDependencies/vicon-datastream-sdk && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/ljb/crazyswarm/ros_ws/src/externalDependencies/libmotioncapture/externalDependencies/vicon-datastream-sdk/Vicon/CrossMarket/DataStream/ViconDataStreamSDK_CPPTest/ViconDataStreamSDK_CPPTest.cpp > CMakeFiles/ViconDataStreamSDK_CPPTest.dir/Vicon/CrossMarket/DataStream/ViconDataStreamSDK_CPPTest/ViconDataStreamSDK_CPPTest.cpp.i

externalDependencies/vicon-datastream-sdk/CMakeFiles/ViconDataStreamSDK_CPPTest.dir/Vicon/CrossMarket/DataStream/ViconDataStreamSDK_CPPTest/ViconDataStreamSDK_CPPTest.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/ViconDataStreamSDK_CPPTest.dir/Vicon/CrossMarket/DataStream/ViconDataStreamSDK_CPPTest/ViconDataStreamSDK_CPPTest.cpp.s"
	cd /home/ljb/crazyswarm/ros_ws/src/externalDependencies/libmotioncapture/build/externalDependencies/vicon-datastream-sdk && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/ljb/crazyswarm/ros_ws/src/externalDependencies/libmotioncapture/externalDependencies/vicon-datastream-sdk/Vicon/CrossMarket/DataStream/ViconDataStreamSDK_CPPTest/ViconDataStreamSDK_CPPTest.cpp -o CMakeFiles/ViconDataStreamSDK_CPPTest.dir/Vicon/CrossMarket/DataStream/ViconDataStreamSDK_CPPTest/ViconDataStreamSDK_CPPTest.cpp.s

# Object files for target ViconDataStreamSDK_CPPTest
ViconDataStreamSDK_CPPTest_OBJECTS = \
"CMakeFiles/ViconDataStreamSDK_CPPTest.dir/Vicon/CrossMarket/DataStream/ViconDataStreamSDK_CPPTest/ViconDataStreamSDK_CPPTest.cpp.o"

# External object files for target ViconDataStreamSDK_CPPTest
ViconDataStreamSDK_CPPTest_EXTERNAL_OBJECTS =

devel/lib/libmotioncapture/ViconDataStreamSDK_CPPTest: externalDependencies/vicon-datastream-sdk/CMakeFiles/ViconDataStreamSDK_CPPTest.dir/Vicon/CrossMarket/DataStream/ViconDataStreamSDK_CPPTest/ViconDataStreamSDK_CPPTest.cpp.o
devel/lib/libmotioncapture/ViconDataStreamSDK_CPPTest: externalDependencies/vicon-datastream-sdk/CMakeFiles/ViconDataStreamSDK_CPPTest.dir/build.make
devel/lib/libmotioncapture/ViconDataStreamSDK_CPPTest: devel/lib/libViconDataStreamSDK_CPP.so
devel/lib/libmotioncapture/ViconDataStreamSDK_CPPTest: /usr/lib/x86_64-linux-gnu/libboost_system.so
devel/lib/libmotioncapture/ViconDataStreamSDK_CPPTest: /usr/lib/x86_64-linux-gnu/libboost_thread.so
devel/lib/libmotioncapture/ViconDataStreamSDK_CPPTest: /usr/lib/x86_64-linux-gnu/libboost_chrono.so
devel/lib/libmotioncapture/ViconDataStreamSDK_CPPTest: /usr/lib/x86_64-linux-gnu/libboost_date_time.so
devel/lib/libmotioncapture/ViconDataStreamSDK_CPPTest: /usr/lib/x86_64-linux-gnu/libboost_atomic.so
devel/lib/libmotioncapture/ViconDataStreamSDK_CPPTest: externalDependencies/vicon-datastream-sdk/CMakeFiles/ViconDataStreamSDK_CPPTest.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/ljb/crazyswarm/ros_ws/src/externalDependencies/libmotioncapture/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable ../../devel/lib/libmotioncapture/ViconDataStreamSDK_CPPTest"
	cd /home/ljb/crazyswarm/ros_ws/src/externalDependencies/libmotioncapture/build/externalDependencies/vicon-datastream-sdk && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/ViconDataStreamSDK_CPPTest.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
externalDependencies/vicon-datastream-sdk/CMakeFiles/ViconDataStreamSDK_CPPTest.dir/build: devel/lib/libmotioncapture/ViconDataStreamSDK_CPPTest

.PHONY : externalDependencies/vicon-datastream-sdk/CMakeFiles/ViconDataStreamSDK_CPPTest.dir/build

externalDependencies/vicon-datastream-sdk/CMakeFiles/ViconDataStreamSDK_CPPTest.dir/clean:
	cd /home/ljb/crazyswarm/ros_ws/src/externalDependencies/libmotioncapture/build/externalDependencies/vicon-datastream-sdk && $(CMAKE_COMMAND) -P CMakeFiles/ViconDataStreamSDK_CPPTest.dir/cmake_clean.cmake
.PHONY : externalDependencies/vicon-datastream-sdk/CMakeFiles/ViconDataStreamSDK_CPPTest.dir/clean

externalDependencies/vicon-datastream-sdk/CMakeFiles/ViconDataStreamSDK_CPPTest.dir/depend:
	cd /home/ljb/crazyswarm/ros_ws/src/externalDependencies/libmotioncapture/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/ljb/crazyswarm/ros_ws/src/externalDependencies/libmotioncapture /home/ljb/crazyswarm/ros_ws/src/externalDependencies/libmotioncapture/externalDependencies/vicon-datastream-sdk /home/ljb/crazyswarm/ros_ws/src/externalDependencies/libmotioncapture/build /home/ljb/crazyswarm/ros_ws/src/externalDependencies/libmotioncapture/build/externalDependencies/vicon-datastream-sdk /home/ljb/crazyswarm/ros_ws/src/externalDependencies/libmotioncapture/build/externalDependencies/vicon-datastream-sdk/CMakeFiles/ViconDataStreamSDK_CPPTest.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : externalDependencies/vicon-datastream-sdk/CMakeFiles/ViconDataStreamSDK_CPPTest.dir/depend

