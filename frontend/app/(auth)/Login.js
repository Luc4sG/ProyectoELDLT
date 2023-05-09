import {View, Text, Pressable, Dimensions, SafeAreaView} from 'react-native';
import React from 'react';
import {COLORS, FONTS, icons} from '../../constants';
import {SvgXml} from 'react-native-svg';
import {Stack, useRouter, useNavigation, useRootNavigation} from 'expo-router';
import { Logo } from '../../components';


const Login = () => {
    const router = useRouter();
    return (
        <SafeAreaView style={{flex:1, backgroundColor: COLORS.background }}>
            <Stack.Screen
                options={{
                    headerShadowVisible: true,
                    headerTitle: "hola",
                }} />
           
        <Logo/>

        </SafeAreaView>
);
}

export default Login;