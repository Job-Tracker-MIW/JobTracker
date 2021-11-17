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
    title: "Jobs",
    path: "/jobs-page",
    icon: <FaIcons.FaBuilding />,
  },
  {
    title: "Language Skills",
    path: "/skills-page",
    icon: <FaIcons.FaTools />,
  },
];