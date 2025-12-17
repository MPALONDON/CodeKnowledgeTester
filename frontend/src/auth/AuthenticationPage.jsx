import "react";
import {SignIn,SignUp,SignedIn,SignedOut} from "@clerk/clerk-react";
import style from "./auth.module.css";

export default function AuthenticationPage(){
    return <div className={style.authContainer}>
        <SignedOut>
            <SignIn routing="path" path="/sign-in"/>
            <SignUp routing="path" path="/sign-up"/>
        </SignedOut>

        <SignedIn>
            <div className={style.redirectMessage}>
                <p>You are already signed in.</p>
            </div>

        </SignedIn>

    </div>
}