import React from "react";
import * as FaIcons from "react-icons/fa";
import * as AiIcons from "react-icons/ai";
import * as IoIcons from "react-icons/io";
  
export const SidebarData = [
  {
    title: "Home",
    path: "/home",
    icon: <AiIcons.AiFillHome />,
  },
  {
    title: "Applied Jobs",
    path: "/applied_jobs",
    icon: <IoIcons.IoIosPaper />,
  },
  {
    title: "Contacts",
    path: "/contacts",
    icon: <FaIcons.FaPhone />,
  },
  {
    title: "Companies",
    path: "/companies",
    icon: <FaIcons.FaBuilding />,
  
    // Maybe will incorporate subgenres of companies? 
    
    // subNav: [
    //   {
    //     title: "Companies 1",
    //     path: "/companies/companies1",
    //     icon: <IoIcons.IoIosPaper />,
    //   },
    //   {
    //     title: "Companies 2",
    //     path: "/companies/companies1",
    //     icon: <IoIcons.IoIosPaper />,
    //   },
    // ],
  },
  {
    title: "Skills",
    path: "/skills",
    icon: <FaIcons.FaTools />,
  },
];