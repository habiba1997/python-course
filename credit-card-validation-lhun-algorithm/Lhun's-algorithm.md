# Luhn Algorithm for Validating Credit Card Numbers

The Luhn algorithm, also known as the "modulus 10" or "mod 10" algorithm, is a simple checksum formula used to validate
a variety of identification numbers, especially credit card numbers. It helps ensure that the entered number is
potentially valid before further processing. The algorithm verifies the numeric validity of the card number rather than
its existence.

1. Sum Odd Index Digits: <br>
   Fetch the odd index digits and sum them

2. Double Even Index Digit: <br>
   Fetch the even index digits and double their values

3. Sum the double even index digits in special way:
   <br> Every 2 digit integer, Sum the values of every single digit in it with the singular digit integer

4. Sum odd sum with even sum and divide by 10: <br>
   Sum the value returned from sum of step 3 and the value of sum from step 1 and divide teh summation with 10

5. Check Validity:
   <br> If the remainder of step 4 is zero =-> then this credit-card is VALID else NOT VALID

Purpose:
The Luhn algorithm isn't foolproof; it won't verify the validity of the credit card account or whether funds are
available. However, it quickly catches common input errors or transposition mistakes when entering the card number.

This algorithm is widely used in many applications to provide a basic level of validation for credit card numbers or
other identification numbers, ensuring they meet a simple criteria before further verification.