import { Navigate, Route, Routes } from 'react-router-dom';
import { Sidebar } from './components/Sidebar';
import { ModulePage } from './pages/ModulePage';
export default function App(){return <div className="app-shell"><Sidebar/><Routes><Route path="/:module" element={<ModulePage/>}/><Route path="*" element={<Navigate to="/dashboard" replace/>}/></Routes></div>}
