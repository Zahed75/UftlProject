
        const opennav = () => {
            document.getElementById("slidenav").style.width = "270px";
            document.getElementById("closeicon").style.display = "block";
        }

        const closenav = () => {
            document.getElementById("slidenav").style.width = "0";
            document.getElementById("closeicon").style.display = "none";
            if (screen.width >= 1240) {
                document.getElementById("menuicon").style.display = "none";
            } else {
                document.getElementById("menuicon").style.display = "block";
            }
        }

        window.addEventListener("resize", (event) => {
            if (document.body.clientWidth >= 1240) {
                document.getElementById("menuicon").style.display = "none";
                document.getElementById("slidenav").style.width = "0px";
            } else {
                document.getElementById("menuicon").style.display = "block";
            }
        })