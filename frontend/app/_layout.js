import { Stack, SplashScreen } from 'expo-router';
import { useFonts } from 'expo-font';

const Layout = () => { 
    const [loaded] = useFonts({
        Hubballi: require('../assets/fonts/Hubballi-Regular.ttf'),
        Montserrat: require('../assets/fonts/Montserrat-Regular.ttf'),
        MontserratBold: require('../assets/fonts/Montserrat-Bold.ttf'),
        Ruluko: require('../assets/fonts/Ruluko-Regular.ttf'),
    });

    if (!loaded) {
        return <SplashScreen/>;
    }

    return (
        <Stack screenOptions={{ 
            headerShown: false }}
        />
    );
};

export default Layout;