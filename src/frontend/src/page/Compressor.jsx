import Main from "../components/Main"
import { Navbar } from "../components/Navbar/Navbar"

import "./Compressor.scss"

export const Compressor = () => {
    return (
        <>
            <Navbar 
                home
            />
            <div className="compressor-wrapper">
                <Main />
            </div>
        </>
    )
}