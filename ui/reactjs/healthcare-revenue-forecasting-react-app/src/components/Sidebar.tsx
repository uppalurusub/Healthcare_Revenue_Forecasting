import { NavLink } from 'react-router-dom';
import { ENDPOINTS } from '../config/endpoints';
import { titleize } from '../utils/formatters';
export function Sidebar() { return <aside className="sidebar"><div className="brand">RCM Analytics</div><nav>{Object.keys(ENDPOINTS).map(m => <NavLink key={m} to={`/${m}`} className={({isActive}) => isActive ? 'active' : ''}>{titleize(m)}</NavLink>)}</nav></aside>; }
