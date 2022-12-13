function 작은수(x, y, z) {
    if (x < y) {
        if (z < x) {
            console.log(z)
        } else {
            console.log(x)
        }
    } else {
        if (z < y) {
            console.log(z)
        } else {
            console.log(y)

        }
    }
}
작은수(1, 3, 5)
작은수(3, 5, 1)
작은수(5, 1, 3)