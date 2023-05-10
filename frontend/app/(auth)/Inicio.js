
import React from "react";
import { SafeAreaView, View, Text, Pressable, Dimensions } from "react-native";
import  Carousel from 'react-native-reanimated-carousel';
import AnimatedDotsCarousel from 'react-native-animated-dots-carousel';
import { Stack, usePathname, useRouter } from "expo-router"
import { SvgXml } from "react-native-svg";
import  Logo  from "../../components/forms/logo/Logo";


//Constantes
import {COLORS, FONTS, icons} from '../../constants';

const Inicio = () => {
    const [index, setIndex] = React.useState(0);
    const router = useRouter();
    const width = Dimensions.get('window').width;
    const handleIndex = (index) => {
        setIndex(index)
    }
    const ruta = usePathname();
  return (
    <SafeAreaView 
            style={{flex:1, backgroundColor: COLORS.background }}>
            <Stack.Screen
                options={{
                    headerShadowVisible: false,
                    headerTitle: "",
                }} />
            
            <Logo/> 
            
            <View style={{  flex: 1, 
                            alignItems: 'center',
                            justifyContent: 'flex-end',

                            }}>
            <Pressable onPress={() => router.push('/Login')}>
                {({ pressed }) => (
                    <Text style={{ textDecorationLine:'underline', marginBottom:8, fontSize: 18, fontFamily: FONTS.Montserrat, color: pressed ? COLORS.fColorGray : COLORS.fColorBlack }}>
                    Iniciar Sesión
                    </Text>
                )}
            </Pressable>    

            <Pressable onPress={() => router.push('/Register')}>
                {({ pressed }) => (
                    <Text style={{ textDecorationLine:'underline', marginBottom:8, fontSize: 18, fontFamily: FONTS.Montserrat, color: pressed ? COLORS.fColorGray : COLORS.fColorBlack }}>
                    Crear una nueva cuenta
                    </Text>
                )}
            </Pressable>
            </View>  

            <View style={{  flex: 1, 
                            justifyContent: 'flex-end',

                         }}>
                 <Carousel
                    loop={false}
                    width={width}
                    height={width / 2}
                    autoPlay={false}
                    mode="parallax"
                    modeConfig={{ parallaxScrollingOffset: 50 }}
                    data={[...new Array(3).keys()]}
                    scrollAnimationDuration={1000}
                    onSnapToItem={(index) => console.log('current index:', index)}
                    onProgressChange={(_, absoluteProgress) => {
                        handleIndex(Math.round(absoluteProgress));}}
                    renderItem={({ index }) => (
                        <View
                            style={{
                                flex: 1,
                                borderWidth: 1,
                                justifyContent: 'center',
                                borderRadius: 10,
                            }}
                        >
                            <Text style={{ textAlign: 'center', fontSize: 30 }}>
                                {index}
                            </Text>
                        </View>
                    )}
                    style={{ alignSelf: 'center' }} 
                />
                    <View style={{flex:2, width: '100%', height: 25,alignItems:'center' }}>
                        <AnimatedDotsCarousel
                        length={3}
                        currentIndex={index}
                        maxIndicators={3}
                        interpolateOpacityAndColor={false}
                        activeIndicatorConfig={{
                        color: '#000000',
                        margin: 3,
                        opacity: 1,
                        size: 8,
                        }}
                        inactiveIndicatorConfig={{
                        color: '#343434',
                        margin: 3,
                        opacity: 0.5,
                        size: 8,
                        }}
                        decreasingDots={[{
                        config: { color: '#343434', margin: 3, opacity: 0.5, size: 4 },
                        quantity: 1,
                        }]}/>
                    </View>
            </View>

    </SafeAreaView>
  );
};

export default Inicio; // asegúrate de exportar el componente Inicio