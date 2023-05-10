import {View, Text, Pressable, Dimensions, SafeAreaView, TextInput, Button} from 'react-native';
import React from 'react';
import {COLORS, FONTS, icons} from '../../constants';
import {SvgXml} from 'react-native-svg';
import {Stack, useRouter, useNavigation, useRootNavigation} from 'expo-router';
import Logo from '../../components/forms/logo/Logo';
import CustomBttn from '../../components/forms/custombttn/CustomBttn';


const Login = () => {
    const router = useRouter();
    return (
        <SafeAreaView style={{flex:1, backgroundColor: COLORS.background }}>
            <Stack.Screen
                options={{
                    headerShadowVisible: false,
                    headerTitle: "",
                }} />
           
        <Logo/>
        
        <View style={{  flex: 1, 
                        alignItems: 'center', 
                        justifyContent: 'flex-end', 
                        paddingBottom:104}}>

            <View>    
                <Text style={{  fontSize: 16, 
                                fontFamily: FONTS.Montserrat, 
                                color: COLORS.fColorGray,
                                alignSelf:"flex-start",
                                marginBottom:8 }}>Email</Text>
                <TextInput 
                    style={{
                        height: 40,  
                        borderWidth: 0,
                        marginBottom: 16,
                        backgroundColor: COLORS.fColorWhite,
                        width: 300,
                        borderRadius: 8,
                        paddingHorizontal: 10,}} 
                    placeholder='Email' />

                <Text style={{  fontSize: 16, 
                                fontFamily: FONTS.Montserrat, 
                                color: COLORS.fColorGray,
                                alignSelf:"flex-start",
                                marginBottom:8 }}>Password</Text>
            
                
                <TextInput
                    style={{
                        height: 40,  
                        borderWidth: 0,
                        marginBottom: 16,
                        backgroundColor: COLORS.fColorWhite,
                        width: 300,
                        borderRadius: 8,
                        paddingHorizontal: 10}}
                    secureTextEntry={true}
                    placeholder='Password' />
                </View>
                
                <CustomBttn title={"Iniciar Sesión"} onPress={() => console.log("test")}/>
        </View>

        </SafeAreaView>
);
}

export default Login;