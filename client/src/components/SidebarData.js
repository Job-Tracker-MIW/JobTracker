import React from "react";
import * as FaIcons from "react-icons/fa";
import * as IoIcons from "react-icons/io";
  
export const SidebarData = [

  {
    title: "Applied Jobs",
    path: "/applied-jobs-page",
    icon: <IoIcons.IoIosPaper />,
  },
  {
    title: "Contacts",
    path: "/contacts-page",
    icon: <FaIcons.FaPhone />,
  },
  {
    title: "Companies",
    path: "/companies-page",
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
    path: "/skills-page",
    icon: <FaIcons.FaTools />,
  },
];