import { View, Text, TextInput} from 'react-native';

import { Logo } from '../logo/Logo';
import { CustomBttn } from '../custombttn/CustomBttn';
import { FONTS,COLORS } from '../../../constants';

export default function LoginForm() {
    return (
        <>
        <Logo/>  

        <View style={{  flex: 1, 
                        alignItems: 'center', 
                        justifyContent: 'flex-end', 
                        paddingBottom:104,}}>

            <View>
                <Text style={{  fontSize: 16, 
                                fontFamily: FONTS.Montserrat, 
                                color: COLORS.fColorGray,
                                alignSelf:"flex-start",
                                marginBottom:8 }}>Nombre Completo</Text>
                <TextInput 
                    style={{
                        height: 40,  
                        borderWidth: 0,
                        marginBottom: 16,
                        backgroundColor: COLORS.fColorWhite,
                        width: 300,
                        borderRadius: 8,
                        paddingHorizontal: 10,}} 
                    placeholder='Nombre Completo'/>

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
                                marginBottom:8 }}>Contraseña</Text>
            
                
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
                    placeholder='Constraseña' />

                <Text style={{  fontSize: 16, 
                                fontFamily: FONTS.Montserrat, 
                                color: COLORS.fColorGray,
                                alignSelf:"flex-start",
                                marginBottom:8 }}>Repetir Contraseña</Text>
            
                
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
                    placeholder='Repetir Contraseña' />
                
                </View>
                
                <CustomBttn title={"Registrarse"} onPress={() => console.log("test")}/>
        </View>
        </>
    )
}