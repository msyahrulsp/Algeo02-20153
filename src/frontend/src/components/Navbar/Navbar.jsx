import "./Navbar.scss"

export const Navbar = ({ home }) => {
    return (
        <div className="navbar">
            <div className="navbar-header">
                <h1 className="navbar-logo">
                    {home ? (
                        <a href="/about">
                            Algeough
                        </a>
                    ) : (
                        <a href="/">
                            Compressor
                        </a>
                    )}
                </h1>
            </div>
        </div>
    )
}