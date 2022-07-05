using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.Rendering;
using Microsoft.EntityFrameworkCore;
using VeterinaryClinic.BL;
using VeterinaryClinicWeb.Data;
using VeterinaryClinicWeb.Models.EF.Interfaces;

namespace VeterinaryClinicWeb.Controllers
{
    public class RaceController : Controller
    {

        private readonly IRaceRepository _raceRepository;
        private readonly ISpecieRepository _specieRepository;

        public RaceController(IRaceRepository raceRepository, ISpecieRepository specieRepository)
        {
            _raceRepository = raceRepository;
            _specieRepository = specieRepository;
        }

        //GET: Race
        public async Task<IActionResult> Index() =>
            View(await _raceRepository.GetAll());

        // GET: Race/Details/5
        public async Task<IActionResult> Details(int id)
        {
            if (await _raceRepository.GetById(id) is Race race)
                return View(race);

            return NotFound();
        }

        // GET: Race/Create
        public async Task<IActionResult> Create()
        {
            ViewData["SpecieId"] = new SelectList(await _specieRepository.GetAll(), "Id", "Name");
            return View();
        }

        // POST: Race/Create
        // To protect from overposting attacks, enable the specific properties you want to bind to.
        // For more details, see http://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]

        public async Task<IActionResult> Create([Bind("Id,Name,SpecieId")] Race race)
        {
            ModelState.Remove(nameof(race.Specie));
            if (ModelState.IsValid)
            {
                await _raceRepository.Add(race);
                return RedirectToAction(nameof(Index));
            }
            ViewData["SpecieId"] = new SelectList(await _specieRepository.GetAll(), "Id", "Name");
            return View(race);
        }

        // GET: Race/Edit/5
        public async Task<IActionResult> Edit(int id)
        {
            if (await _raceRepository.GetById(id) is Race race)
            {
                ViewData["SpecieId"] = new SelectList(await _specieRepository.GetAll(), "Id", "Name");
                return View(race);
            }
            return NotFound();
        }

        // POST: Race/Edit/5
        // To protect from overposting attacks, enable the specific properties you want to bind to.
        // For more details, see http://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Edit(int id, [Bind("Id,Name,SpecieId")] Race race)
        {
            if (id != race.Id)
                return NotFound();

            ModelState.Remove(nameof(race.Specie));
            if (ModelState.IsValid)
            {
                try
                {
                    await _raceRepository.Update(race);
                }
                catch (DbUpdateConcurrencyException)
                {
                    throw;
                }
                return RedirectToAction(nameof(Index));
            }
            ViewData["SpecieId"] = new SelectList(await _specieRepository.GetAll(), "Id", "Name");
            return View(race);
        }

        // GET: Race/Delete/5
        public async Task<IActionResult> Delete(int id)
        {
            if (await _raceRepository.GetById(id) is Race race)
                return View(race);

            return NotFound();
        }

        // POST: Race/Delete/5
        [HttpPost, ActionName("Delete")]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> DeleteConfirmed(int id)
        {
            if (await _raceRepository.GetById(id) is Race race)
                await _raceRepository.Delete(race);

            return RedirectToAction(nameof(Index));
        }

    }
}
