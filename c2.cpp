#include <iostream>
#include "config.h"
#include "json.hpp"


CONFIG* Conf = new CONFIG;
int main() 
{
	std::string res((char*) CONFIG_BUFFER);
	config_initialize(Conf, res);
	std::cout << Conf->Hostname << " " << Conf->Migrate;
}
