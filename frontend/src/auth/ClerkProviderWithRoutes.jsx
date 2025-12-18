import {ClerkProvider} from "@clerk/clerk-react";
import {BrowserRouter} from "react-router-dom";

const PUBLISHABLE_KEY = import.meta.env.VITE_CLERK_PUBLISHABLE_KEY
const FRONTEND_URL = import.meta.env.VITE_FRONTEND_URL

if (!PUBLISHABLE_KEY) {
  throw new Error('Missing Publishable Key')
}

export default function ClerkProviderWithRoutes({children}){
    return(
        <ClerkProvider
            publishableKey = {PUBLISHABLE_KEY}
            afterSignInUrl={FRONTEND_URL}
            afterSignUpUrl={FRONTEND_URL}
            afterSignOutUrl={`${FRONTEND_URL}/sign-in`}
            navigate={(to) => (window.location.href = to)}>
            <BrowserRouter>{children}</BrowserRouter>
        </ClerkProvider>
    )
}

