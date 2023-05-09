import { Tabs } from "expo-router";
import { Text } from "react-native";

const TabsLayout = () => {
  return (
    <Tabs
      screenOptions={{
        headerShown: false,
      }}
    >
      <Tabs.Screen
        name="Home"
        options={{
          title: "Home",
          tabBarIcon: () => <Text>Home</Text>,
        }}
      />
      {/* <Tabs.Screen
        name="settings"
        options={{
          title: "Settings",
          tabBarIcon: () => <Text>⚙️</Text>,
        }}
      /> */}
    </Tabs>
  );
};

export default TabsLayout;