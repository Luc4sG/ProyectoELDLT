import {SafeAreaView, ScrollView, KeyboardAvoidingView} from 'react-native';
import { KeyboardAwareScrollView } from 'react-native-keyboard-aware-scroll-view'
import React from 'react';
import {COLORS} from '../../constants';
import {Stack, useRouter} from 'expo-router';
import  LoginForm  from '../../components/forms/loginForm/LoginForm';



const Register = () => {
    const router = useRouter();

    return (
        <SafeAreaView style={{flex:1, backgroundColor: COLORS.background }}>
            <Stack.Screen
                options={{
                    headerShadowVisible: true,
                    headerTitle: "hola",
                }} />
        <ScrollView
            bounces={false}
            contentInsetAdjustmentBehavior="always"
            overScrollMode="always"
            showsVerticalScrollIndicator={true}
            style={{flex:1, backgroundColor:COLORS.red}}>

        <KeyboardAwareScrollView>
            <LoginForm/>
        </KeyboardAwareScrollView>

        </ScrollView>                
        </SafeAreaView>
);
}

export default Register;