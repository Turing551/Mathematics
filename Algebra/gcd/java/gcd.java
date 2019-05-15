import java.math.BigInteger;

public class GreatestCommonDivisor{
    public static int getGCD(int num1, int num2){
         return BigInteger.valueOf(num1).gcd(BigInteger.valueOf(num2)).intValue();
    }
}
