import { useRootNavigationState } from "expo-router";
import { View, Text } from "react-native";
import { useRouter, useSegments } from "expo-router";
import { AuthStore } from "../redux";
import React from "react";

const Index = () => {
    const router = useRouter();
    const segments = useSegments();
    const rootNavigationState = useRootNavigationState();
    const { isLoggedIn } = AuthStore.useState((s)=>s);

    React.useEffect(() => {
        if (!rootNavigationState?.key)return;

        const inAuthGroup = segments[0] === "(auth)";
        //Si el usuario no esta logeado y el path no esta en el grupo 
        if (!isLoggedIn && !inAuthGroup) {
            router.replace("/(auth)/Inicio");
        } else if (isLoggedIn) {
            router.replace("/(tabs)/Home/Home");
        } }
    , [rootNavigationState?.key, isLoggedIn, segments, router]);

    return <View>{!rootNavigationState?.key ? 
        <Text>Loading...</Text> : <></>  //TODO: Add loading screen
     }</View>;
};

export default Index;