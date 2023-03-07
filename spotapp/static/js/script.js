const navigationHeight =
    document.querySelector("#explore-header").offsetHeight + 64

// console.log(navigationHeight)

document.documentElement.style.setProperty(
    "--scroll-padding",
    navigationHeight + "px"
)
