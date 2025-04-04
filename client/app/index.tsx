import React from "react";
import { Link, useRouter } from "expo-router";
import { navigate } from "expo-router/build/global-state/routing";
import { useEffect } from "react";
import { StatusBar, Text, TouchableOpacity, View } from "react-native";

export default function Index() {
    const router = useRouter(); // to navigate

    useEffect(() => {
        setTimeout(() => {
            router.replace("/auth/login");
        }, 3000);
    }, []);

    return (
        <>
            <StatusBar hidden={true} />
            <View className="flex-1 justify-center items-center bg-secondary">
                <Text className="text-6xl font-extrabold italic text-primary">
                    VIBE
                </Text>
            </View>
        </>
    );
}
