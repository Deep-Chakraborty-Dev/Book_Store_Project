import { createContext, useContext, useEffect, useState } from 'react'
import { auth } from "../firebase/firebase.config";
import { createUserWithEmailAndPassword, signInWithEmailAndPassword, GoogleAuthProvider, signInWithPopup, signOut} from 'firebase/auth';
import { onAuthStateChanged } from 'firebase/auth';

const AuthContext = createContext();
export const useAuth = () => {
    return useContext(AuthContext)
}

const googleprovider = new GoogleAuthProvider();

export const AuthProvide = ({children}) => {

    const [currentUser , setCurrentUser] = useState(null);
    const [loading,setLoading] = useState(null);

    const registerUser = async (email,password) => {
        return await createUserWithEmailAndPassword(auth,email,password)
    }

    const loginUser = async (email,password) => {
        return await signInWithEmailAndPassword(auth,email,password)
    }

    const signInWithGoogle = async (email,password) => {
        return await signInWithPopup(auth,googleprovider)
    }

    const logout = () => {
        return signOut(auth)
    }

    useEffect(() => {
        const unsubscribe = onAuthStateChanged(auth, (user) => {
            setCurrentUser(user);
            setLoading(false);

            if(user){
                const {email,displayName,photoURL} = user
                const userData = {
                    email:email,
                    userName:displayName,
                    photo:photoURL
                }
            }
        })
        return () => unsubscribe();
    },
    [])

    const value= {
        currentUser,
        registerUser,
        loginUser,
        loading,
        signInWithGoogle,
        logout
    }

    return(
        <AuthContext.Provider value={value}>
            {children}
        </AuthContext.Provider>
    )
}