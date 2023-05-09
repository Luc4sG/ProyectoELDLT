import React from "react";
import { SafeAreaView, Text } from "react-native";
import { Stack } from "expo-router";

const Home = () => {
  return (
    <SafeAreaView style={{flex:1, backgroundColor: '#DEECDB' }}>
                <Stack.Screen
                     options={{
                         headerStyle: { backgroundColor:'#DEECDB' },
                         headerShadowVisible: false,
                         headerTitle: "Home",
                     }} />
      <Text>Home</Text>
    </SafeAreaView>
  );
};

export default Home; // asegúrate de exportar el componente Inicio