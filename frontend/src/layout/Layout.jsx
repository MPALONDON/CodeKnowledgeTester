import "react";
import {SignedIn,SignedOut,UserButton} from "@clerk/clerk-react";
import {Outlet, Link, Navigate} from "react-router-dom";
import style from "./layout.module.css";

export default function Layout(){
    return <div className={style.appLayout}>
        <header className={style.appHeader}>
            <div className={style.headerContent}>
                <h1>Code Knowledge Tester</h1>
                <nav>
                    <SignedIn>
                        <Link to="/">Generate Challenge</Link>
                        <Link to="/history">History</Link>
                        <UserButton></UserButton>
                    </SignedIn>
                </nav>
            </div>
        </header>
        <main className={style.appMain}>
            <SignedOut>
                <Navigate to="/sign-in" replace/>
            </SignedOut>
            <SignedIn>
                <Outlet></Outlet>
            </SignedIn>

        </main>

    </div>
}