import {View, Text} from 'react-native';
import { SvgXml } from 'react-native-svg';
import {icons, COLORS, FONTS} from '../../../constants'

export default function Logo()  {
    return (
        <>
            <SvgXml xml={icons.xmlLogo} width="50%" height="20%" 
            style={{ alignSelf: 'center', marginLeft: 'auto', marginRight: 'auto', marginTop: 32}} />
            <Text style={{ alignSelf: 'center', fontSize: 20, fontFamily:FONTS.Hubballi, color: COLORS.fColorBlack }}>
                U-BOOK
            </Text>
            <View style={{ flexDirection: 'row', alignSelf: 'center' }}>
                <Text style={{ fontSize: 20, fontFamily: FONTS.Ruluko, color: COLORS.fColorBlack }}>Stay </Text>
                <Text style={{ fontSize: 20, fontFamily: FONTS.Ruluko, color: COLORS.fColorGreen }}>Organized</Text>
            </View>
            <SvgXml xml={icons.xmlBlob2} width="50%" height="50%"
            style={{ position: 'absolute', top: 150, left: 330, right: 0, bottom: 0, zIndex: -1,
            opacity:80}} />
             <SvgXml xml={icons.xmlBlob2} width="50%" height="50%"
            style={{ position: 'absolute', top: 0, left: -130,  zIndex: -1,
            opacity:80}} />
        </>
    )
};

