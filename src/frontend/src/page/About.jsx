import { Navbar } from "../components/Navbar/Navbar"

import "./About.scss"

export const About = () => {
    return (
        <>
            <Navbar />
            <div className="about-wrapper">
                <p className="about-text">Disini perkenalan</p>
            </div>
        </>
    )
}