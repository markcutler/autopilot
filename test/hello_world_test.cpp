#include "autopilot/hello_world.hpp"

#include <gtest/gtest.h>

TEST(Example, HelloWorld) { EXPECT_EQ("Hello World!", GetPrintStatement()); }

int main(int argc, char **argv) {
  ::testing::InitGoogleTest(&argc, argv);
  return RUN_ALL_TESTS();
}