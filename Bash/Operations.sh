#!/bin/bash

read -p "Enter first value: " n
read -p "Enter Second value: " m

echo "The sum is:" $(($n + $m))
echo "The difference  is:" $(($n - $m))
echo "The product is:" $(($n * $m))
echo "The quotient is:" $(($n / $m))
