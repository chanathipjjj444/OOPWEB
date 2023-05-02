import {useState, useContext,createContext} from 'react'

const AuthContext = createContext()

const AuthProvider = ({children}) => {
    var [auth,setAuth] = useState({
        user:"",
        email:"",
        auth:""

        // success:"",
    });
    return (
        <AuthContext.Provider value={[auth, setAuth]}>
            {children}
        </AuthContext.Provider>
    );
};

const useAuth = () => useContext(AuthContext);

export { useAuth, AuthProvider};