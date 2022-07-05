using Microsoft.EntityFrameworkCore;
using VeterinaryClinic.BL;
using VeterinaryClinicWeb.Data;
using VeterinaryClinicWeb.Models.EF.Interfaces;

namespace VeterinaryClinicWeb.Models.EF.Repositories
{
    public class AnimalResponsibleRepository : RepositoryBase<AnimalResponsible>, IAnimalResponsibleRepository
    {
        public AnimalResponsibleRepository(BancoContext context) : base(context) { }
    }
}