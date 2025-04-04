import { View, Text } from "react-native";
import React from "react";
import { useLocalSearchParams } from "expo-router";

const MovieDetailScreen = () => {
    const { id } = useLocalSearchParams();

    return (
        <View>
            <Text>{id}</Text>
        </View>
    );
};

export default MovieDetailScreen;
