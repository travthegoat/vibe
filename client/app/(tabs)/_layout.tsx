import { View, Text } from "react-native";
import React from "react";
import { Tabs } from "expo-router";

const TabLayout = () => {
    return (
        <Tabs>
            <Tabs.Screen name="home/index" options={{ headerShown: false }} />
            <Tabs.Screen name="reviews/index" options={{ headerShown: false }} />
            <Tabs.Screen name="profile/index" options={{ headerShown: false }} />
        </Tabs>
    );
};

export default TabLayout;
