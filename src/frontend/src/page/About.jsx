import { Navbar } from "../components/Navbar/Navbar"
import FotoVito from "../images/vito.png"
import FotoZian from "../images/zian.png"
import FotoSP from "../images/sp.png"

import "./About.scss"

export const About = () => {
    const gitHubLink = 
        "https://github.com/msyahrulsp/Algeo02-20153"
    const openGithub = () => {
        window.open(gitHubLink, "_blank")
    }
    return (
        <>
            <Navbar />
            <div className="about-wrapper">
                <p>Made by</p>
                <div className="about-container">
                    <img src={FotoVito} alt="foto" onClick={() => openGithub()} />
                    <div className="about-text">
                        <ul>Vito Ghifari</ul>
                        <ul>13520153</ul>
                        <ul>K03</ul>
                        <ul>Image Compression</ul>
                    </div>
                </div>
                <div className="about-container-reverse">
                    <div className="about-text">
                        <ul>M Syahrul Surya Putra</ul>
                        <ul>13520161</ul>
                        <ul>K03</ul>
                        <ul>FE</ul>
                    </div>
                    <img src={FotoSP} alt="foto" onClick={() => openGithub()}/>
                </div>
                <div className="about-container">
                    <img src={FotoZian} alt="foto" onClick={() => openGithub()}/>
                    <div className="about-text">
                        <ul>Ghazian Tsabit Alkamil</ul>
                        <ul>13520165</ul>
                        <ul>K03</ul>
                        <ul>FE and BE Handler</ul>
                    </div>
                </div>
            </div>
        </>
    )
}