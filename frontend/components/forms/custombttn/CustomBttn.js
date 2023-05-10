import { View, Button, StyleSheet, TouchableOpacity, Text } from "react-native";
import { FONTS,COLORS } from "../../../constants";
TouchableOpacity.defaultProps = { activeOpacity: 0.8 };

export default function CustomBttn({ onPress, title }) {
    return (
  <TouchableOpacity onPress={onPress} style={styles.appButtonContainer}>
    <Text style={styles.appButtonText}>{title}</Text>
  </TouchableOpacity>
);};

const styles = StyleSheet.create({
    appButtonContainer: {
      elevation: 3,
      backgroundColor: COLORS.fColorPrimary,
      borderRadius: 6,
      paddingVertical: 10,
      paddingHorizontal: 12,
    },
    appButtonText: {
      fontSize: 16,
      color: COLORS.fColorBlack,
      fontFamily: FONTS.Montserrat,
      alignSelf: "center",
    }
  });