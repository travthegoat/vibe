import { View, Text, TextInput } from "react-native";
import React from "react";

const AuthForm = ({ func }) => {
    return (
        <View className="w-full p-4">
            <View className="w-full flex flex-row bg-neutral-200">
                <TextInput
                    placeholder="Enter Your Username"
                    className="w-full"
                />
            </View>
        </View>
    );
};

export default AuthForm;
