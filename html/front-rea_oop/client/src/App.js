
import './App.css';
import {Routes,Route} from 'react-router-dom'
import HomePage from './pages/HomePage';
import About from './pages/About';
import Register from './pages/Auth/Register';
import Login from './pages/Auth/Login';
import Showroom from './pages/Showroom';
import Addon from './pages/Addon';
import PeopleForm from './pages/PeopleForm';
import Bill from './pages/Bill';
import Showhotel from './pages/Showhotel';
import AdminDashboard from './pages/AdminDashboard';
import CreateHotel from './pages/CreateHotel';
import CreateRoom from './pages/CreateRoom';
import ManageUser from './pages/ManageUser'
import CreateAddons from './pages/CreateService';


function App() {
  return (
   <>
   <Routes>
    <Route path="/" element={<HomePage/>}/>
    <Route path="/about" element={<About/>}/>
    <Route path="/register" element={<Register/>}/>
    <Route path="/login" element={<Login/>}/>
    <Route path="/showroom" element={<Showroom/>}/>
    <Route path="/addon" element={<Addon/>}/>
    <Route path="/insertdata" element={<PeopleForm/>}/>
    <Route path="/billupdate" element={<Bill/>}/>
    <Route path="/showhotel" element={<Showhotel/>}/>
    <Route path="/admin" element={<AdminDashboard/>}/>
    <Route path="/admin/manage-hotel" element={<CreateHotel/>}/>
    <Route path="/admin/manage-room" element={<CreateRoom/>}/>
    <Route path="/admin/manage-addons" element={<CreateAddons/>}/>
   </Routes>
   </>
  );
}

export default App;
