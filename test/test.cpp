#include <gtest/gtest.h>

TEST(Example, Test1) {
    EXPECT_EQ(2, 5-3);
}

int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}