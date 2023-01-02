package algo

/// Modulo returns "python" like modulo:
/// Modulo(5, 3)	=	2
/// Modulo(5, -3)	=	-1
/// Modulo(-5, 3)	=	1
/// Modulo(-5, -3)	=	-2
func Modulo(a, m int) int {
	return ((a % m) + m) % m
}
