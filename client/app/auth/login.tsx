import { View, Text, StatusBar, TextInput } from "react-native";
import React from "react";
import AuthForm from "../../components/AuthForm";

const LoginScreen = () => {
    return (
        <>
            <StatusBar hidden={true} />
            <View className="flex-1 bg-secondary items-center justify-center">
                <Text className="text-7xl font-extrabold text-primary italic">
                    VIBE
                </Text>

                <AuthForm func={''}/>
            </View>
        </>
    );
};

export default LoginScreen;
